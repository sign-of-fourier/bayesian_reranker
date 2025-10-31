

navbar = """

<title>{} by Quante Carlo</title>
<div class="navbar">

    <a href="/">Home</a>
    <div class="subnav">
        <button class="subnavbtn">How it works</a><i class="fa fa-caret-down"></i></button>
        <div class="subnav-content">
            <a href="https://medium.com/@markshipman4273/the-best-rerankers-24d9582c3495">Retrieval as a Bayesian Optimization Problem</a>
            <a href="https://medium.com/@markshipman4273/">Generative Engine Optimization using Monte Carlo Tree Search</a>
        </div>
        
    </div>
    <a href='https://github.com/sign-of-fourier/bayesian_reranker'>Build your own</a>
    <a href='https://www.quantecarlo.com/get-started'>Contact us</a>

</div>




<div class="header">
    <p align="right">
    <table>
        <tr><td><h1>{}</h1></td>
            <td> &nbsp; &nbsp; &nbsp; &nbsp; </td><td rowspan=2>
            <img src="https://static.wixstatic.com/media/614008_6006e77a45db4c8ea97da77bc26cca7c~mv2.jpg/v1/fill/w_123,h_123,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/qc%20logo.jpg"></img></p>
            </td>
        </tr>
        <tr><td align="right">by Quante Carlo</td><td> &nbsp; </td>
        </tr>
    </table>
    </p>
</div>



"""



webpage_main = """
{}

<body>
{}
<div class="column row"></div>

<div class="column tenth"></div>

<div class="column fifth">
  <div class="card">
  <font size=+3><b>50 Credits</b></font><br>
  <br><br>
  <font size="+3">$39</font><br>
  <form action='https://buy.stripe.com/test_8x23cvcVz1V831dfEwbjW00'>
  <input type="submit" name="product" value="Checkout">
  </form>
  </div>
</div>

<div class="column tenth"></div>

<div class="column fifth">
  <div class="card"><font size="+3">
    <b>Subscription</b></font><br>
    100 credits per month<br><br>
    <font size="+3">$59</font><br>
    <form action='stripe'>
    <input type="submit" name="product" value="Checkout">
    </form>
  </div>
</div>

<div class="column tenth"></div>

<div class="column fifth">
  <div class="card">
  <font size="+3"><b>Enterprise</b><br></font>
  Custom<br><br>
  <font size="+2">Starting at $1000</font><br>
  <form action='/email'>
  <input type="submit" name="product" value="Contact Us">
  </form>
  </div>
</div>

<div class="column tenth"></div>


</html>
"""




style="""
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>

* {
  box-sizing: border-box;
}


body {
  margin: 1;
  /*background-color: aliceblue;*/
  background-image: linear-gradient(to bottom right, aliceblue , white);
}

/* Style the header */
.header {
  background-image: linear-gradient(to bottom left, #edebec, #b6b5ba);
  /*background-color: #b6b5ba;*/
  padding: 20px;
  text-align: center;
}

/* Style the top navigation bar */
.topnav {
  overflow: hidden;
  background-color: #0f314d;
}

/* Style the topnav links */
.topnav a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.navbar {
  overflow: hidden;
  background-color: #0f314d;
}
.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.subnav {
  float: left;
  overflow: hidden;
}

.subnav .subnavbtn {
  font-size: 16px;
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}
.topnav a:hover {
  background-color: #ddd;
  color: black;
}
.navbar a:hover, .subnav:hover .subnavbtn {
  background-color: #edebec;
  color: black;
}

.subnav-content {
  display: none;
  position: absolute;
  left: 0;
  background-color: #edebec;
  width: 100%;
  z-index: 1;
}

.subnav-content a {
  float: left;
  color: black;
  text-decoration: none;
}

.subnav-content a:hover {
  background-color: #eee;
  color: black;
}

.subnav:hover .subnav-content {
  display: block;
}

.column {
  float: left;
  padding: 10px;
}
.column.left {
  background-color: aliceblue;
  width: 15%;
  height: 500px;
  overflow: auto;
}
.column.middle {
  /*border: 1px solid black;*/
  width: 80%;
  /*background-color: cornsilk;*/
  height: 500px;
  overflow: auto;
  border-radius: 10px;
  box-shadow: 4px 8px 16px rgba(0, 0, 0, 0.15);

  /*border-radius: 30px;*/
}
.column.half {
  width: 50%;
  overflow: auto:
}
.column.small {
  border: 0px solid purple;
  width: 5%;
  bacground-color: aliceblue;
}
.column.tenth {
  width: 10%;
}
.column.middle_top {

  border: 0px;
  height: 40%;
  width: 100%;
  overflow: auto;
}

.column.middle_middle {
  height: 50%;
  width: 100%;
  border-radius: 10px;
  background-color: blanchedalmond;
  overflow: auto;
}

.column.middle_bottom{
  border: 0px solid orange;
  height: 10%;
  overflow: auto;
  width: 100%;
}
.column.fifth{
  border: 0px solid green;
  width: 20%;
}

.column.middle_big {
  width: 90%;
  border: 0px solid white;
  border-radius: 10px;
  padding: 8px;
}
.column.row {
   height: 1px;
   width: 100%;
}


.rounded {
    border: 1px solid cadetblue;
    height:380px;
    border-radius: 15px;
}

.shaded {
    background: gainsboro;
    border: 1px solid cadetblue;
    border-radius: 10px;
    box-shadow: 4px 8px 16px rgba(0, 0, 0, 0.15);

}
.card {
    background-image: radial-gradient(ghostwhite, ivory, floralwhite);
    border: 1px solid cadetblue;
    border-radius: 10px;
    box-shadow: 4px 8px 16px rgba(0, 0, 0, 0.15);
    text-align: center;
}


img {
    border: 1px solid #e3e3e3;
    /*border: 1px solid #b6b5ba;*/
}


/* Clear floats after the columns */
.row::after {
  content: "";
  display: table;
  clear: both;
}


</style>
"""

script = """<script>
document.getElementById('reranker').addEventListener('submit', function(event) {
  document.getElementById('submit').disabled = true;
  document.getElementById('submit').textContent = 'Submitting...';
  submit();
  //event.preventDefault();
  //form.submit();
});
</script>

"""



chooser = """
{}
<body>
{}
<div class="column row"> &nbsp; </div>
<div class="column left"></div>
<div class="column middle">
<table><tr><td><font +1><b>Generateive Engine Optimization:</b> </font><a href="/geomcts">GEO</a></td><td>Uses Monte Carlo Tree Search to write and rewrite articles to increase relevance with respect to Cohere's Reranker.</td></tr>
  <tr><td></td></tr>
  <tr><td><font size=+1><b>Bayesian Reranker for</b></font><a href=\"/reranker\"> RAG</font></a></td><td>Uses parallel Bayesian Optimiation to iteratively, irmprove the retrieval step.</td></tr>
</table>

</div>

<div class = "column right"></div>
"""







geomcts_home="""<html>
{}
<body>
{}

<div class="column left"></div>
<div class="column middle">

    <table border=0>
        <tr>
            <td colspan=2> <h3>This demo uses Parallel Bayesian Optimization to increase context at each iteration for RAG using the miniwiki
            <a href="https://huggingface.co/datasets/rag-datasets/rag-mini-wikipedia">dataset</a>. </h3></td>
        </tr>
        <tr><td colspan=2> &nbsp; </td></tr>
        <tr>
            <td colspan=2><form id="geomcts" action="/initialize_drafts" method=POST>
                 <textarea name=topic rows=3 cols=80>Describe the athletic differences between football and baseball.</textarea>
            </td>
        </tr>
        <tr>
            <td colspace=2>
            </td>
        </tr>
        <tr>
            <td>
                <input id="Rewrite" type="submit" name="write" value="Write"></input>
            </td>
            <td>
            </td>
        <tr>
        <tr>
            <td colspan=2>
                <textarea name=article rows=4 cols=80>Optional: you can start with your own article but, the topic is still required.</textarea>
            </td>
        <tr>
            <td>
                <input id="Rewrite" type="submit" name="write" value="Rewrite"></input>
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td>
                 Depth of rollout:
                &nbsp;
                <select name="tree_depth">
                    <option value="3">3</option>
                    <option value="5">5</option>
                    <option value="8">8</option>
                    <option value="10">10</a>
               </select>

            </td>

            <td>Number of initial trees:
                &nbsp;
                <select name="n_trees">
                    <option value="3">3</option>
                    <option value="5">5</option>
                    <option value="8">8</option>
                    <option value="10">10</a>
               </select>
        </td>
        </tr>
        </form>
        <tr>
            <td colspan=2><hr></td>
        </tr>
        <tr>
            <td colspan=2>
            <h4>How it works</h4>
            <ol>
                <b>Write:</b>
                <li> Writes stories based on your topic and then looks for a score</li>
                <li> Performs a roll out: sequentially rewrites the story.</li>
                <li> Scores eaach story based on Cohere's <a href="https://cohere.com/rerank">reranker </a></li>
                <li> Uses Bayesian Optimization based on the embeddings of the stories to estimate the best place for a new node.</li>
                <i>Performs rollouts in parallel </i><br>
                <b>Rewrite:</b>
                <li> Same as before but instead of writing from scratch, it starts by rewriting the story you provide.<br>
            </ol>
            </td>
        </tr>
    </table>
</div>
<div class="column right"></div>
{}
</html>



"""

geomcts_iterate = """
{}
<body>
{}
<div class="column row"> &nbsp; </div>
<div class="column left">{}</div>
<div class="column middle">
<table>
    <form id="geomcts" action="/geo_mcts" method=POST>
    
    {}
    <tr><td colspan=2>
    {}
    </td>
    <tr><td></td><td><input id="submit" type=submit value="optimize"></td></tr>
</form>
</table>
</div>
{}
<div class = "column right"></div>
"""


home="""
<html>
{}
<body>
{}

<div class="column left"></div>
<div class="column middle">

    <table border=0>
        <tr>
            <td colspan=2> <h3>This demo uses Parallel Bayesian Optimization to increase context at each iteration for RAG using the miniwiki 
            <a href="https://huggingface.co/datasets/rag-datasets/rag-mini-wikipedia">dataset</a>. </h3></td>
        </tr>
        <tr><td colspan=2> &nbsp; </td></tr>
        <tr>
            <td colspan=2><form id="reranker" action="/improve_question" method=POST>
                 <textarea name=query rows=3 cols=80>Tell me about wolves in Europe.</textarea>
            </td>
        </tr>
        <tr>
        <td>
             <input id="submit" type="submit" name="submit" value="improve">
        </td>

        <td>Number of results per keyword term to fetch from corpus:
            &nbsp;
            <select name="n_results">
                <option value="3">3</option>
                <option value="5">5</option>
                <option value="8">8</option>
                <option value="10">10</a>
            </select>
        </td>
        </tr>
        </form>
        <tr>
            <td colspan=2><hr></td>
        </tr>
        <tr>
            <td colspan=2>
            <h4>How it works</h4>
            <ol>
                <b>First screen:</b>
                <li> Rewrites your prompt</li>
                <li> Comes up with search terms based on the improved prompt</li>
                <li> Performs an embedding based search (chroma db) based on the more detailed search terms</li>
                <b>Second screen:</b>
                <li> On the first iteration, the best few based on the embedding search are chosen<br>
                There is an llm scorer in the background that rates the relevance, reliability and recenty of the retrieved documents.</li>
                <li> For each iteration after that, batch Bayesian Optimization is performed to decide what are the next best choices based on what's been learned about the retrieval's so far.</li>
            </ol>
            </td>
        </tr>
    </table>
</div>
<div class="column right"></div>
{}
</html>
"""

optimization_page = """
{}
<body>
{}
<div class="column row"> &nbsp; </div>
<div class="column left">{}</div>
<div class="column middle">
<table>
    <form id="reranker" action="/optimize" method=POST>
    <tr><td>Improved Question</td><td> {} <input type=hidden name=improved_question value="{}"></td></tr>
    <tr><td>{}</td><td>{}</td></tr>
    {}

    <tr><td></td><td><input id="submit" type=submit value="optimize"></td></tr>
</form>
</table>
</div>
{}
<div class = "column right"></div>
"""


hidden = "<input type=hidden name=\"{}\" value=\"{}\"></input>\n"


quante_carlo = """<html>
<body>
<table>
    <tr>
        <td><a href="/reranker">Reranker</a></td>
    </tr>
    <tr>
        <td><a href="https://medium.com/@markshipman4273/dspy-is-slow-heres-how-to-make-it-fast-632bd85afb75">DSPy accelerator</a></td>
    </tr>
    <tr>
        <td><a href="https://quantecarlo.com">Quante Carlo</a></td>
    </tr>
</table>
</html>
"""

