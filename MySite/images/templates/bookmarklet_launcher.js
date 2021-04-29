(function(){
if (window.myBookmarklet !== undefined){
myBookmarklet();
}
else {
document.body.appendChild(
document.createElement('script')
).src='https://7777c4cd59f9.ngrok.io:8000/static/js/bookmarklet.js?r=' + Math.floor(Math.random()*99999999999999999999);
}
})();