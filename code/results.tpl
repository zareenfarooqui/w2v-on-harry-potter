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

  <style>
      #myProgress {
        position: relative;
      }

      #myBar {
        position: absolute;
      }

      div.myCenteredTable {
        text-align: center;
      }
      
      div.myCenteredTable table {
        margin: 0 auto;
        text-align: left;
      }

  </style>


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

    
    <br> 
    <div class="progress" id="myProgress">
      <div class="progress-bar progress-bar-success" id="myBar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width:0%">
      </div>
    </div>

    
    % word2display = word
    <div class="myCenteredTable container">
      <h3 class="text-center">The 7 most similar words to '{{word2display}}' are:</h3>
      <br>

      <div class="myCenteredTable table-responsive col-md-6 col-md-offset-3">
    		<table class="table table-bordered text-center table-striped">
          <thead>
            <tr>
              <th class="text-center" width="70%">word</th>
              <th class="text-center" width="30%">cosine distance</th> 
            </tr>
          </thead>
          <tbody>
      		%for x in rows:
      		  <tr>
      		  %for y in x:
      		    <td class="text-center">{{y}}</td>
      		  %end
      		  </tr>
      		%end
      		</tbody>	
    		</table>
      </div>

    </div>
    <br>
    <br>
    <h4 class="text-center">Want to learn more? <br> <a href="http://www.blog.zareenfarooqui.com" target="_blank"> Read my blog</a></h4>
    <br>
    <br>

  </body>

</html>

