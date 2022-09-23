# Public portal - Nginx configuration



**Inspired by**

* [dhis2 docs](https://docs.dhis2.org/en/manage/performing-system-administration/dhis-core-version-238/installation.html#install_making_resources_available_with_nginx)
* [Stackoverflow: Can nginx location blocks match a URL query string?](https://serverfault.com/a/811981)

## Setup

For **one** chart.

### `query_string`

the analytics API call from one chart in DHIS2. Make sure it is URL decoded, e.g. with [an online tool](https://www.urldecoder.org/).

### `Authorization` header

The `Authorization` header can be created in the Browser console, paste the following:

```javascript
"Basic " + btoa('username:secretPassword')
```
use a restricted user.

The result should look something like `"Basic YWRtaW46ZGlzdHJpY3Q=";`


### Nginx config

Config for one chart (`@chart1`) - use the data created above to fill in details for `nginx.conf`:


```
    location ~ /api/analytics {
      error_page 418 = @chart1;
      
      if ( $query_string = "dimension=bOCrZguqyBl:trJaHzeHYnM;y0wlxDf8qDR;yP3GrmbXDRC&dimension=pe:LAST_12_MONTHS&showHierarchy=false&hierarchyMeta=false&includeMetadataDetails=true&includeNumDen=true&skipRounding=false&completedOnly=false&outputIdScheme=NAME&filter=ou:USER_ORGUNIT,dx:dQxo7a1fQNL") { return 418; }
    }

    location @chart1 {
      proxy_pass         http://localhost:8080;
      proxy_redirect     off;
      proxy_set_header   Host               $host;
      proxy_set_header   X-Real-IP          $remote_addr;
      proxy_set_header   X-Forwarded-For    $proxy_add_x_forwarded_for;
      proxy_set_header   X-Forwarded-Proto  http;
      proxy_set_header   Authorization      "Basic YWRtaW46ZGlzdHJpY3Q=";
      proxy_set_header   Cookie             "";
      proxy_hide_header  Set-Cookie;
    }

```

Apply it: `nginx -t && nginx -s reload`

### More charts

Each chart should get its own `error_page` using its own **non-standard** HTTP code (e.g. 418-499), `if` directive, and `location`.

