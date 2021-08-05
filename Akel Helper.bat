@ECHO OFF
call "%USERPROFILE%\Anaconda3\Scripts\activate.bat" "%USERPROFILE%\Anaconda3"
call conda activate "P:\Support\Admin\Timesheets\Denver Noell_MISC\work_scripts\Akel_helper\akel_helper"
cd "P:\Support\Admin\Timesheets\Denver Noell_MISC\work_scripts\Akel_helper"
call streamlit run streamlit_helper.py
start http://localhost:8501