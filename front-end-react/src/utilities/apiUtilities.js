export function setCookie(cname, cvalue, hours) {
    let d = new Date();
    d.setTime(d.getTime() + (hours * 60 * 60 * 1000)); // (exdays * 24 * 60 * 60 * 1000));
    let expires = 'expires=' + d.toUTCString();
    document.cookie = cname + '=' + cvalue + ';' + expires + ';path=/';
}

export function getCookie(cname) {
    let name = cname + '=';
    let ca = document.cookie.split(';');

    for(let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) ===' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }

    return '';
}


export function removeCookie(cookie_name){
    if( getCookie( cookie_name ) ) {
        document.cookie = cookie_name + "=" +
            ";path=/" +
            ";expires=Thu, 01 Jan 1970 00:00:01 GMT";
    }
}

export function clearCookies(){
    let cookies = document.cookie.split("; ");
    for (let c = 0; c < cookies.length; c++) {
        let d = window.location.hostname.split(".");
        while (d.length > 0) {
            let cookieBase = encodeURIComponent(cookies[c].split(";")[0].split("=")[0]) + '=; expires=Thu, 01-Jan-1970 00:00:01 GMT; domain=' + d.join('.') + ' ;path=';
            let p = window.location.pathname.split('/');
            document.cookie = cookieBase + '/';
            while (p.length > 0) {
                document.cookie = cookieBase + p.join('/');
                p.pop();
            }
            d.shift();
        }
    }
}

export function baseUrl(endpoint) {
    let base = 'http://localhost:8000/'
    return `${base}${endpoint}`;
}