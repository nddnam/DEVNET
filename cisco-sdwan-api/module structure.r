VMANAGE_AUTHENTICATION <- vmanage_host, vmanage_port, vmanage_username, vmanage_password
 .get_header
 .get_baseurl

devices_monitor
 .devicelist    <- none
 .controlcheck  <- system_ip

cli_template 
 .checkattached <- template_name
 .getid         <- template_name
 .getconfig     <- template_name
 .getname       <- system_ip
