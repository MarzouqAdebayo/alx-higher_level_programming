$.getJSON(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    data.results.forEach((film) => {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  }
);
