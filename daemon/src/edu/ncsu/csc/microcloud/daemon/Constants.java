package edu.ncsu.csc.microcloud.daemon;


public class Constants {
	
	public static final String MSG_TYPE = "msg_type";
	public static final String MSG_TYPE_REGISTER = "register";
	public static final String MSG_TYPE_UNREGISTER = "unregister";
	public static final String MSG_IS_ALIVE = "is_alive";
	
	public static final String PARENT_IP = "parent_ip";
	public static final String PARENT_PORT = "parent_port";
	public static final String CHILD_PORT = "child_port";
	public static final String POLLING_PERIOD = "polling_period";
	public static final String DB_HOSTNAME = "db_hostname";
	public static final String DB_NAME = "db_name";
	public static final String DB_USERNAME = "db_username";
	public static final String DB_PASSWORD = "db_password";
	public static final String DB_DRIVER = "db_driver";
	public static final String DB_URI = "jdbc:mysql://";
	public static final String DEFAULT_PARENT_IP = "localhost";
	public static final String DEFAULT_PARENT_PORT = "9000";
	public static final String DEFAULT_CHILD_PORT = "9090";
	public static final String DEFAULT_POLLING_PERIOD = "300000";

    public static final String CHILD_SCRIPT_PATH = "child_script_path";
    public static final String PARENT_SCRIPT_PATH = "parent_script_path";
	public static final String DEFAULT_CHILD_SCRIPT_PATH = 
                            "../../../diff-resources/Initial Setup/child.py";
    public static final String DEFAULT_PARENT_SCRIPT_PATH = 
                            "../../../diff-resources/Initial Setup/parent.py";

	public static final String OK_MESSAGE = "OK";
	
	public static final String CHILD_CONFIG_FILE = "child_config.properties";
	public static final String PARENT_CONFIG_FILE = "parent_config.properties";
}
