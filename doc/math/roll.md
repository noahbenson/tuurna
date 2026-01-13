(math:rollapp)=
# Roll Some Dice!

This page lets you {{roll}} some dice as if you were making a {{check}} for a
{{skill}}.  Below, the on the right correspond to the {{level}} of the
{{skill}} being {{rolled}}. If you click on one of these numbers, an example
{{roll}} result and {{score}} will be shown. The score is shown in the middle
and individual dice are shown on the right, where losses are colored red, wins
are colored green, and explosions are colored cyan.

<!-- Here we include style information used in the app -->
<style>
  span.expdie {
    width: 24px;
    heigh: 24px;
    background-color: black;
    color: cyan;
    border: 2px solid cyan;
  }
  span.windie {
    width: 24px;
    heigh: 24px;
    background-color: black;
    color: green;
    border: 2px solid green;
  }
  span.lossdie {
    width: 24px;
    heigh: 24px;
    background-color: black;
    color: red;
    border: 2px solid red;
  }
  span.blankdie {
    width: 24px;
    heigh: 24px;
  }
  div.cursed {
    width: 50%;
    height: 60px;
    background-color: #888888;
    color: #121212;
    border: 2px solid #121212;
  }
  div.disadvantaged {
    width: 50%;
    height: 60px;
    background-color: #888888;
    color: #121212;
    border: 2px solid #121212;
  }
  div.neutral {
    width: 50%;
    height: 60px;
    background-color: #888888;
    color: #121212;
    border: 2px solid #121212;
  }
  div.advantaged {
    width: 50%;
    height: 60px;
    background-color: #888888;
    color: #121212;
    border: 2px solid #121212;
  }
  div.blessed {
    width: 50%;
    height: 60px;
    background-color: #888888;
    color: #121212;
    border: 2px solid #121212;
  }
  button.roll {
    font-size: 16px;
    text-align: center;
    vertical-align: middle;
    border-radius: 4px;
    cursor: pointer;
  }
  button.roll:hover {
    background-color: #9999aa;
  }
  table.buttons {
    width: 128px;
    height: 100%;
    border-collapse: separate;
  }
  table.layout {
    width: 100%;
    height: 100%;
    border: none;
    border-collapse: separate;
    border-spacing: 72px 0px;
  }
  td.leftcell {
    width: 128px;
    height: 200px;
    border: none;
  }
  td.midcell {
    width: 128px;
    height: 200px;
    border: none;
    text-align: center;
    vertical-align: top;
  }
  td.rightcell {
    width: 100%;
    height: 200px;
    border: none;
    text-align: left;
    vertical-align: top;
  }
  td.button {
    width: 24px;
    height: 24px;
    text-align: center;
    vertical-align: middle;
  }
  div.rollapp {
    width: 600px;
    height: 200px;
  }
  th.title {
    height: 36px;
    text-align: center;
    vertical-align: top;
    font-weight: bold;
  }
  p.title {
    height: 36px;
    text-align: center;
    vertical-align: top;
    font-weight: bold;
  }
  div.results {
    width: 90%;
    max-height: 180px;
    height: 180px;
    overflow-x: hidden;
    overflow-y: auto;
    font-size: 14px;
    box-sizing: border-box;
    text-align: left;
  }
  p.score {
    font-weight: bold;
    font-size: 14pt;
    text-align: center;
  }
  p.dicerow {
    font-size: 14pt;
    text-align: left;
    vertical-align: top;
    margin: 6px;
  }
</style>

<center><div class="rollapp" id="theRollApp">
  <table class="layout"><tr>
    <td class="leftcell"><table class="buttons">
      <th class="title" colspan=3>Skill Level</th>
      <tr>
        <td class="button"><button class="roll" id="r1">1</td>
        <td class="button"><button class="roll" id="r2">2</td>
        <td class="button"><button class="roll" id="r3">3</td></tr>
      <tr>
        <td class="button"><button class="roll" id="r4">4</td>
        <td class="button"><button class="roll" id="r5">5</td>
        <td class="button"><button class="roll" id="r6">6</td></tr>
      <tr>
        <td class="button"><button class="roll" id="r7">7</td>
        <td class="button"><button class="roll" id="r8">8</td>
        <td class="button"><button class="roll" id="r9">9
          </td></tr></table></td>
    <td class="midcell">
      <p id="scoretag" class="title">Score</p>
      <p id="score" class="score"> </p></td>
    <td class="rightcell"><div class="results">
      <p class="title" id="dicetag">Dice</p>
      <p class="dicerow" id="dicerow1"> </p>
      <p class="dicerow" id="dicerow2"> </p>
      <p class="dicerow" id="dicerow3"> </p>
      <p class="dicerow" id="dicerow4"> </p>
      <p class="dicerow" id="dicerow5"> </p>
      <p class="dicerow" id="dicerow6"> </p>
      <p class="dicerow" id="dicerow7"> </p>
      <p class="dicerow" id="dicerow8"> </p>
      <p class="dicerow" id="dicerow9"> </p>
      </div></td></table></div></center>

<script>
  const scoreP = document.getElementById('score');
  const scoreTag = document.getElementById('scoretag');
  // Select the button and message elements from the HTML
  for (let ii = 1; ii < 10; ii++) {
    const button = document.getElementById('r' + ii);
    button.addEventListener('click', function() {
      dice = [];
      score = 0;
      for (let jj = 1; jj < 10; jj++) {
        rs = [];
        const row = document.getElementById('dicerow' + jj);
        row.replaceChildren();
        if (jj > ii)
            continue;
        do {
          r = Math.floor(Math.random() * 6) + 1;
          rs.push(r);
          const span = document.createElement('span');
          span.textContent = ('' + r);
          if (r > 4) {
            score++;
            span.classList.toggle('expdie', true);
          } else if (r > 2) {
            score++;
            span.classList.toggle('windie', true);
          } else {
            span.classList.toggle('lossdie', true);
          }
          row.appendChild(span);
          const blank = document.createElement('span');
          blank.innerHTML = '&nbsp;';
          blank.classList.toggle('blankdie', true);
          row.appendChild(span);
          row.appendChild(blank);
        } while (r > 4 && rs.length < 11);
        dice.push(rs);
      }
      if (score > 10) {
        score = 10;
      }
      scoreP.textContent = `${score}`;
    });
  }
</script>

