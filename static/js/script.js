function getBotResponse() {
          var rawText = $("#textInput").val();
          var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
          $("#textInput").val("");
          $("#chatbox").append(userHtml);
          document
            .getElementById("userInput")
            .scrollIntoView({ block: "start", behavior: "smooth" });
          $.get("/get", { msg: rawText }).done(function(data) {
            var img = '<img src="https://icon-library.com/images/bot-icon/bot-icon-7.jpg" alt="BOT" style="width:80px;height:60px;"/>'
            var botHtml = '<p class="botText"> ' + img + ' <span>' + data + "</span></p>";
            $("#chatbox").append(botHtml);
            document
              .getElementById("userInput")
              .scrollIntoView({ block: "start", behavior: "smooth" });
          });
        }
        $("#textInput").keypress(function(e) {
          if (e.which == 13) {
            getBotResponse();
          }
 });