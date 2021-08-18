from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command

nr = InitNornir(
    config_file = "config.yaml", dry_run=True
)

s1=nr.run(netmiko_send_config, config_file= "IOSXRv.txt")
s2=nr.run(netmiko_send_config, config_commands=["interface lo 9", "description Equipo6NornirConPython","ipv4 add 9.9.7.8 255.255.255.255", "commit"])
s3=nr.run(netmiko_send_command, command_string="do show ip int brief")
print_result(s1)
print_result(s2)
print_result(s3)