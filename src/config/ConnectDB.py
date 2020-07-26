import pydoc

class ConfigDB:
    def __init__(self, cnxn, cursor):
        
        self.cnxn = pydoc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=server_name;"
            "Database=db_name;"
            "Trusted_Connection=yes;"
        )

        self.cursor = cnxn.cursor()
