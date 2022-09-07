from configparser import ConfigParser
import os

"""
            EasyConf
            Author:sobhan-kz-01
"""





class Config:
    """ Config Tools """
    def __init__(self,file_name,file_type,create_now=False):
        self.config = ConfigParser()
        self.BASE_DIR = os.getcwd()
        self.FILE_DIR = f'{self.BASE_DIR}\{file_name}.{file_type}'
        self.create_now = create_now
        self.ERROR = 'Incorrect Information'
        if os.path.isfile(self.FILE_DIR):
            self.config.read(self.FILE_DIR)

        if self.create_now == True:
            if os.path.isfile(self.FILE_DIR):
                self.create_now = False
            else:
                with open(self.FILE_DIR,'w') as config_file:
                    self.config.write(config_file)

    def write(self):
        with open(self.FILE_DIR,'w') as config_file:
            self.config.write(config_file)

    def load(self,file_dir,default_dir=True):
        if default_dir:
            self.config.read(self.FILE_DIR)
        else:
            self.config.read(file_dir)    

    def create_section(self,section,key={}):
        """  section:[Section] | key = value 
             YOU CAN PASS KEY WITH ZIP : 
             keys = ['key1','key2','key3']
             values = ['value1','value2','value3']
             key = dict(zip(keys,values)) """

        
        exists = self.config.has_section(section)
        if not exists:
            self.config[section] = key
            self.write()


    def add_key(self,section,key,value):
        """ Key  = Value """


        item = self.config[section]
        try:
            is_exists = item.get(key)
            if not is_exists:
                item[key] = value    
        except:
            item[key] = value
        self.write()

    def query_value(self,section,key):
        """ Query Value 
            [Section]
            Key = Value """
        
        try:
            item = self.config[section]
        

            query = item.get(key)
            return query
        except:
            
            return self.ERROR
        
    
    def query_key(self,section,key):
        """ Query Key
            [Section]
            Key = Value """
        
        try:

            query = self.config[section]
            value = query.get(key)
            item = key + ' = ' + value
            return item
        except:
            
            return self.ERROR
        
        

    def query_all_keys(self,section,return_list_value=False):
        """ Query All Keys In Section """
        try:

            if return_list_value == False:
                keys = self.config[section]
                item = ''
                for key in keys:
                    value = keys.get(key)
                    item += key+' = '+value+'\n'
                return item
            elif return_list_value:
                keys = self.config[section]
                item = []
                for key in keys:
                    item.append(key)
                return item
        except:
            return self.ERROR        



    def strict_key(self,section,key,value,defualt_value):
        try:
            query = self.query_key(section,key)
            
            not_change = False
            for i in value:
                item = ''.join(i)
                final = key + ' = ' + item
                if query == final:
                    not_change = True
                    break
            
            if not_change == False:
                self.config[section][key] = defualt_value
                self.write()
        except:
            
            return self.ERROR


    
    
    def is_section_exists(self,section):
        try:

            if section in self.config:
                return True
            else:
                return False
        except:
            
            return self.ERROR            


    def is_value_exists(self,section,key,value):
        try:

            item = self.config[section].get(key)

            if item == value:
                return True
            else:
                return False
        except:
            
            return self.ERROR
    

    def is_key_exists(self,section,key):
        try:

            item = self.config[section]
            if item.get(key):
                return True
            else:
                return False
        except:
            
            return self.ERROR  