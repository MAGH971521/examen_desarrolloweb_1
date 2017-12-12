function getParameterByName(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

  $(document).ready(function(){
    var query = getParameterByName('q');
    console.log(query);
    var nextLibroUrl;

    function attachTweet(libroValue, prepend){
      var libroPublicacion = libroValue.timesince;
      var libroTitulo = libroValue.Titulo;
      var libroAutores = libroValue.Autores;
      var libroEditoria = libroValue.Editorial;
      var libroSinopsis= libroValue.Sinopsis;
      var libroId = libroValue.id;
      if (prepend==true){
        $('#ajax_tweets').prepend(
          "<div class='card' style='width: 20rem;'>"+
            "<div class='card-body'>"+
              "<h4 class='card-title'>Titulo</h4>"+
              "<h6 class='card-subtitle mb-2 text-muted'>Autores</h6>"+
              "<p class='card-text'>Sinopsis Corta</p>"+
              "<a href='#' class='card-link'>Detalles</a>"+
            "</div>"+
          "</div>"
        )
      }else{
        $("#ajax_libros").append(
        )
      }
    }
    function fetchLibros(url){
      console.log("fetching...");
      var fetchUrl;
      if (!url){
        fetchUrl='/api/libro/?q=somequery';
      }else{
        fetchUrl=url
      }

      $.ajax({
        url: fetchUrl,
        data:{
          'q': query
        },
        method: "GET",
        success: function(data){
          // console.log(data);
          nextLibroUrl = data.next;
          $.each(data.results, function(key, value){
            var libroKey = key;
            attachTweet(value);
          });
        },
        error: function(data){
          console.log("error");
          console.log(data);
        }
      });
    }

    fetchLibros();

    $("#loadmore").click(function(event){
      event.preventDefault();
      console.log("click me")
      if (nextLibroUrl){
        fetchTweets(nextLibroUrl);
      }
    })
  });
