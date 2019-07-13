README
======

- Python 3.6

Install
-------

1. Create a new environment

   `conda create -n DecisiveWorkflowResearch python=3.6`

2. Activate it

   `conda activate DecisiveWorkflowResearch`

3. Install requirements

   `pip install -r requirements.txt`

4. Launch Jupyter notebook (ensure you are in the same directory as this README)

   `jupyter notebook &`

  - You will see your browser open to this directory

5. Access this notebook in the 'notebooks' directory: 20190703-DA-WORKFLOW-01.01-basic_plot.ipynb

  - This will download data and plotting code

6. Click Cell -> Run All to run the plot in Jupyter notebook
7. If successful, send a screenshot to the the #promotion channel upgraded to the next level

   - Please be patient as not all helpers may be online

8. (Optional) Move to the SETUP section for notebook git setup

Setup
-----

This setup will apply a output stripping filter before checking in notebooks.
Alternatively, you may manually strip your notebooks with nbstripout before commiting to remove the output

1. After you have installed the pip requirements, move to step 2

   - If you have not, run `pip install nbstripout`

2. Open `.git/config` in your editor, and add this
        [filter "nbstripout"]
            clean = "/path/to/nbconvert/nbstripout"

   - For example:
        [filter "nbstripout"]
            clean = "/c/Users/YOURNAME/AppData/Local/Continuum/anaconda3/envs/DecisiveWorkflowResearch/Scripts/nbstripout.exe"

3. (Optional) Manually run `nbstripout <notebook>` before commiting


Notebook Naming
---------------

Format is `YYYYMMDD-YOURID-WORKFLOW-NN.NN-any_name_with_underscores.ipynb`

- Replace YOURID with your initials or Server username
- Replace NN.NN with the workflow per the Quant Skill Map
- Replace any_name_with_underscores with a description of the notebook

Data
----
The standard data timeframe will be 5-minute CSV files, processed into binary parquet.

If you'd like access to more instruments, drop me a note in the Server and I'll process back-adjusted futures contracts into parquet format (filesize is easier to handle)

Backtesting
-----------

pip install "backtrader[plotting]"
