$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  function getTranslate () {
    const lang = $('INPUT#language_code').val();
    $.getJSON(url + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').on('click', getTranslate);
});
