%#template to generate a table of w2v results (10 most similar words)
<!DOCTYPE html>
<html lang="en">

  <head>
    <title>Word2Vec - Harry Potter</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

    <script>
    function validateForm() {
      userWord = document.forms["W2Vcontinue"]["submittedWord"].value;
      var notOneWord = /\b \b/.test(userWord);
      //show error message if more than one word submitted 
      if (notOneWord == true) {
        document.getElementById("moreThanOneWord").innerHTML = "Enter only one word."
        return false;
        }
      //trims any leading or trailing whitespace 
      var anyWhiteSpace = /\s/.test(userWord);
      if (anyWhiteSpace == true) {
        document.forms["W2Vcontinue"]["submittedWord"].value = userWord.trim();
        }
      }
    </script>

    <script>
    //loads progress bar
      function move() {
        var elem = document.getElementById("myBar");
        var width = 1;
        var id = setInterval(frame, 80);
        function frame() {
          if (width >= 100) {
            clearInterval(id);
          } else {
            width++;
            elem.style.width = width + '%';
          }
        }
      }
    </script>

  </head>
  <body>

   <div>
        <ul class="breadcrumb">
          <li><a href="http://www.zareenfarooqui.com">Home</a></li>
          <li><a href="http://www.zareenfarooqui.com/projects">Projects</a></li>
          <li class="active">HP W2V</li>        
        </ul>
    </div>
    <div class="jumbotron">
        <h1 class="text-center">Word2Vec</h1>      
        <p class="text-center">Type in a word to find the 7 most similar words from the Harry Potter series.</p>
    </div>

    % word2display = word
    <div class="alert alert-danger text-center">
      <strong>Try another word!</strong> "{{word2display}}" was not found in the 7 Harry Potter books.
    </div>
  
    <div class="container text-center">
      <form class="form-inline" name="startW2V" role="form" action="http://52.38.76.106:8080/w2v" 
      onsubmit="return validateForm()" method="POST">
        <div class="form-group input-group-lg">
          <input type="text" name="submittedWord" class="form-control" placeholder="Word to analyze..." required>
        </div>
        <button type="submit" class="form control btn btn-default btn-lg" onclick="move()">Submit</button>
      </form>
     </div> 

    <p id="moreThanOneWord" class="text-center text-danger"></p>

    <style>
      #myProgress {
        position: relative;
      }

      #myBar {
        position: absolute;
      }
    </style>
    <br> 
    <div class="progress" id="myProgress">
      <div class="progress-bar progress-bar-success" id="myBar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width:0%">
      </div>
    </div>

  </body>

</html>

