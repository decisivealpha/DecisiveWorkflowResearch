README
======

- Python 3.6

Install
-------

1. Create a new environment (conda create -n DecisiveWorkflowResearch python=3.6)
2. Activate it (conda activate DecisiveWorkflowResearch)
3. Install requirements (pip install -r requirements.txt)
4. Access notebook: 20190703-DA-WORKFLOW-01.02-basic_plot.ipynb
  - (this will download data and plotting code)
5. Run the plot in Jupyter notebook
6. If successful, send a screenshot to the the #promotion channel upgraded to the next level (please be patient)

Usage
-----

1. Strip your notebooks with nbstripout before commiting to remove the output
  - To easily strip your notebook outputs, 'pip install nbstripout' and add this to your .git/config:
        [filter "nbstripout"]
            clean = "/path/to/nbconvert/nbstripout"
  - Alternatively, you can run 'nbstripout <notebook>'
