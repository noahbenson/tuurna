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
    display: inline-block;
    width: 32px;
    heigh: 16px;
    font-size: 12pt;
    background-color: black;
    color: cyan;
    border: 2px solid cyan;
    text-align: center;
    vertical-align: middle;
  }
  span.windie {
    display: inline-block;
    width: 32px;
    heigh: 26px;
    font-size: 12pt;
    background-color: black;
    color: green;
    border: 2px solid green;
    text-align: center;
    vertical-align: middle;
  }
  span.lossdie {
    display: inline-block;
    width: 32px;
    heigh: 16px;
    font-size: 12pt;
    background-color: black;
    color: red;
    border: 2px solid red;
    text-align: center;
    vertical-align: middle;
  }
  span.blankdie {
    display: inline-block;
    font-size: 14pt;
    width: 16px;
    heigh: 16px;
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
    height: 200px;
    border-collapse: separate;
  }
  table.layout {
    width: 100%;
    height: 100%;
    border: none;
    border-collapse: separate;
    border-spacing: 12px 0px;
  }
  td.leftcell {
    width: 96px;
    height: 412px;
    border: none;
    vertical-align: top;
  }
  td.midcell {
    width: 64px;
    height: 412px;
    border: none;
    text-align: center;
    vertical-align: top;
  }
  td.rightcell {
    width: 100%;
    height: 412px;
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
    height: 412px;
    border: 1px solid #777777;
    border-radius: 4px;
  }
  p.title {
    height: 28px;
    text-align: left;
    vertical-align: top;
    font-weight: bold;
    font-size: 16pt;
  }
  div.results {
    width: 400px;
    max-width: 600px;
    height: 400px;
    overflow-x: auto;
    overflow-y: hidden;
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
    <td class="leftcell">
      <p class="title">Skill Level</p>
      <table class="buttons">
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
            </td></tr></table>
        <form id="rollfate">
          <input type="radio" id="cursed" name="fate" value="cursed">
          <label for="cursed">Cursed</label><br/>
          <input type="radio" id="disadv" name="fate" value="disadv">
          <label for="disadv">Disadvantaged</label><br/>
          <input type="radio" id="neutral" name="fate" value="neutral" checked>
          <label for="neutral">Neutral</label><br/>
          <input type="radio" id="adv" name="fate" value="adv">
          <label for="adv">Advantaged</label><br/>
          <input type="radio" id="blessed" name="fate" value="blessed">
          <label for="blessed">Blessed</label><br/></form></td>
    <td class="midcell">
      <p id="scoretag" class="title">Score</p>
      <p id="score" class="score"> </p></td>
    <td class="rightcell">
      <p class="title" id="dicetag">Dice</p>
      <div class="results">
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
    const form = document.getElementById('rollfate');
    button.addEventListener('click', function() {
      const fate = form.elements['fate'].value
      if (fate == 'cursed') {
        expmin = 7;
        winmin = 3;
      } else if (fate == 'disadv') {
        expmin = 6;
        winmin = 3;
      } else if (fate == 'neutral') {
        expmin = 5;
        winmin = 3;
      } else if (fate == 'adv') {
        expmin = 5;
        winmin = 2;
      } else {
        expmin = 5;
        winmin = 1;
      }
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
          if (r >= expmin) {
            score++;
            span.classList.toggle('expdie', true);
          } else if (r >= winmin) {
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
        } while (r >= expmin && rs.length < 11);
        dice.push(rs);
      }
      if (score > 10) {
        score = 10;
      }
      scoreP.textContent = `${score}`;
    });
  }
</script>

