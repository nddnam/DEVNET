VMANAGE_AUTHENTICATION <- vmanage_host, vmanage_port, vmanage_username, vmanage_password
 .get_header
 .get_baseurl

DEVICES
 .devicelist    <- none
 .controlcheck  <- system_ip

CLI_TEMPLATE
 .checkattached <- template_name
 .getid         <- template_name
 .getconfig     <- template_name
 .getname       <- system_ip
