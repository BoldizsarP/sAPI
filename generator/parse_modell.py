from models.config import Base

class ParsedModell():

    def __init__(self, orm_modell):
        self.orm = orm_modell
    
    @staticmethod
    def parse_yaml(orm_modell:Base):
        """
        First stage of implementation
        Handle
        - unqiue
        - nullable
        - primary key
        - String, Int, UUID, Date and Datetime

        Second Stage of implementation
        Handle
        - foreign key
        - one2one relation
        
        Third Stage of implementation
        Handle
        - simple hierarchy
        - inheritance of acces levels

        Parameters
        ----------
        orm_modell : _type_
            _description_
        """
        
        return [
            
                {
                    "name":orm_modell.__class__.__name__


            } for table in orm_modell.metadata.tables
        ]