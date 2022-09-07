# config-tools
The easy way to work with config files in python 3


# Start
  from config_tools import Config

  config = Config('file_name','file_type') => file_type like ini or cfg

# Create Section 

      can pass key and value with zip

key = ['key1','key2','key3']

value = ['value1','value2','value3']

dicts = dict(zip(key,value))

config.create_section(section='SECTION',key=dicts)


# Strict Key
can check value if value is not correct value can set default value

config.strict_key(section='SECTION',key='key',value=['value1','value2'],default_value='defualt')


# Add Key

config.add_key('SECTION','new_key','value')

# Query Value

function will return value

config.query_value('SECTION','key')

# Query Key

config.query_key('SECTION','KEY')

# Query All Keys

config.query_all_keys('SECTION')


# Exists Functions

functions will return True or False

example:

    """ section """

    is_exsists = config.is_section_exists('SECTION')

    print(is_exists) ===> True

    more:

        is_value_exists
        
        is_key_exists
