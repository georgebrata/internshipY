/**
 * Created by user on 3/11/2016.
 */

function set_openid(openid, pr) {
    u = openid.search('<username>')
    if (u != -1) {
        // openid requires username
        user = prompt('Enter your ' + pr + ' username:')
        openid = openid.substr(0, u) + user
    }
    form = document.forms['login'];
    form.elements['openid'].value = openid
}
