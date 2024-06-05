Deploy shiny app to modal based on streamlit example - https://github.com/modal-labs/modal-examples/tree/main/10_integrations/streamlit

To create the shiny app:

pip install shiny

shiny create 

select basic app

shiny run app.py


currently get an error: modal-http: internal server error: status Failure: TimeoutError('Waited too long for port 8000 to start accepting connections. Make sure the web server is listening on all interfaces, or adjust `startup_timeout`.') when running modal serve 
