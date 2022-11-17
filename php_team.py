from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("PHP_Team", show=False, direction="TB"):
    ELB("Olivier") >> [
        EC2("Christophe"),
        EC2("Jason"),
        EC2("Niki"),
        EC2("Rudy"),
        EC2("Stijn") ] >> RDS("Évènements")
