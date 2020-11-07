import subprocess as sub
import os
os.system("tput setaf 6")
print('Welcome in to My Menu Program To Make Life Symple')
print("-----------------------------------------")
os.system("tput setaf 7")
while 5>4 :
	yourChoice = int(input("""Chose a category in which field you want to work
	1.Configer YUM
	2.Docker
	3.create partation
	4.LVM
	5.hadoop
	6.httpd
	7.Exit
	"""))
	if yourChoice == 1:
		print("please wet a second")
		a = sub.getstatusoutput("yum install firefox")
		if a[0] == 0:
			print("yum is already configered")
			input("Press Enter to contineu")
			os.system("clear")
		else:
			sub.getstatusoutput("echo '[dvd1] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream \ngpgcheck=0 \n\n[dvd2] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS \ngpgcheck=0' > yumconfi.repo | mv yumconfi.repo /etc/yum.repos.d/")
			print("yum is configred in yumcondi.repo file")
			input("Press Enter to contineu")
			os.system("clear")
	
	elif yourChoice == 2:
		while 5>4 :
			dockerInput=int(input("""what do you do in docker
		1.install docker
		2.Start Docker service
		3.Status of Docker
		4.Download docker image in your OS
		5.See the list of docker images installed in your OS
		6.Install docker image in your pc
		7.Boot any os which you installed already
		8.terminet docker image
		9.Exit 
		"""))
			if dockerInput == 1:
				os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")		
				os.system("dnf install docker-ce --nobest")
				input("Press Enter to contineu")
				os.system("clear")
			elif dockerInput == 2:
				os.system("systemctl start docker")
				input("Press Enter to contineu")
				os.system("clear")
			elif dockerInput == 3:
				os.system("systemctl status docker")
				input("Press Enter to contineu")
				os.system("clear")
			elif dockerInput == 4:
				sub.getoutput("systemctl start docker")
				imgName = input("enter full name of image which you want to download(for eg: centos:7): ")
				os.system("docker pull {}".format(imgName))
				os.system("docker images")
				input("Press Enter to contineu")
				os.system("clear")
			elif dockerInput == 5:
				os.system("docker images")
				input("Press Enter to contineu")
				os.system("clear")
			elif dockerInput == 6:
				os.system("docker image")
				imgName = input("Enter full name of Docker Image(For eg: centos:7): ")	
				osName = input("Enter Your Image Name(for eg:kapil): ")
				os.system("docker run -it -name {} {}".format(osName,imgName))
				input("Press Enter to contineu")
				os.system("clear")
			elif dockerInput == 7:
				os.system("docker ps")
				sub.getoutput("systemctl start docker")
				dockerId = input("enter any ony OS Name or OS ID: ")
				so.system("docker start {}".format(dockerId))
				os.system("docker attach {}".format(dockerId))
				input("Press Enter to contineu")
				os.system("clear")
			elif dockerInput == 8:
				os.system("docker ps")
				sub.getoutput("systemctl start docker")
				dockerId = input("enter any ony OS Name or OS ID: ")
				so.system("docker rm {}".format(dockerId))
				input("Press Enter to contineu")
				os.system("clear")
			elif dockerInput == 9:
				break
	elif yourChoice == 3:
		while 5>4 :
			partitionChoice = int(input("""What do you want
		1.create or delete the partition
		2.to see all the disk present in your pc
		3.to see all mounted disk present in your pc
		4.exit
		"""))
			if partitionChoice == 1:
				os.system("fdisk -l")
				diskName = input("Enter disk name which you want to use for create partition (like sda,sdc,sdb etc: )")
				print(""" ----- FOR HELP -----
		p. To see the details of your disk.
		n. To create new partition.
		d. TO delete partition.
		w. To save changes.
		""")
				os.system("fdisk /dev/{}".format(diskName))
				os.system("udevadm settle")
				os.system("lsblk")
				diskNumber = int(input("how many partition you create: "))
				if diskNumber == 0:
					break
				else :
					for i in range(diskNumber-1):
						name = ['first','second','third','fourth','fifth','sixth','seventh','eighth','neneth']
						partLoca = input("enter your {} partition name which you created (like sdc1): ".format(name[i]))
						partName = input("in which directory you want to mount: ")
						confirm = sub.getstatusoutput("mkdir {}".format(partName))
						while confirm[0] != 0:
							partName = input("this directory {} esists. Type again directory name: ".format(partName))
							confirm = sub.getstatusoutput("mkdir {}".format(partName))
						os.system("mkfs.ext4 /dev/{}".format(partLoca))
						os.system("mount /dev/{} {}".format(partLoca,partName))	
						input("Press Enter to contineu")
						os.system("clear")
			elif partitionChoice ==2:
				os.system("fdisk -l")
				input("Press Enter to contineu")
				os.system("clear")
			elif partitionChoice ==3:
				os.system("df -h")
				input("Press Enter to contineu")
				os.system("clear")
			elif partitionChoice ==4:
				break
			else:
				print("invalid input try again")
	elif yourChoice == 4:
		while 5>4 :
			lvmChoice = int(input("""What Do You Want In LVM
		1.Create or Delete Logical Partiton
		2.Extend Partition Size.
		3.Reduce Partition Size.
		4.Extend Virtual Grouph Size.
		5.exit."""))
			if lvmChoice == 1:
				os.system("fdisk -l")
				b=int(input("enter how many storage you want to attech:"))
				c=[]
				for i in range(b):
					d=input("enter the name of storage {}".format(i+1))
					c.append(d)
					os.system("pvcreate /dev/{}".format(d))
				e=input("please enter virtual grouph name: ")
				os.system("vgcreate {} /dev/{}".format(e,c[0]))
				x = range(b)
				x.pop(0)
				for p in x:
					os.system("vgextend {} /dev/{}".format(e,c[p]))
				f=int(input("enter partition size: "))
				g=input("enter your paraition name: ")
				os.system("lvcreate --size {}G --name {} {}".format(f,g,e))
				os.system("mkfs.ext4 /dev/{}/{}".format(e,g))
				h=input("enter a directory name where you want to mount this partition: ")
				os.system("mkdir {}".format(h))
				os.system("mount /dev/{}/{} {}".format(e,g,h))
				print("your partition was created sussfully")
				a=input("do you want to see details of your storage? (y/n): ")
				if a in 'y':
					os.system("lvdisplay {}/{}".format(e,g))
				input("Press Enter to contineu")
				os.system("clear")
			elif lvmChoice == 2:
				e=input("please enter virtual grouph name: ")
				g=input("enter your paraition name (for example sdd2): ")
				l=int(input("enter how much size you want to increase: "))
				os.system("lvextend --size +{}G /dev/{}/{}".format(l,e,g))
				os.system("resize2fs /dev/{}/{}".format(e,g))
				input("Press Enter to contineu")
				os.system("clear")
			elif lvmChoice == 3:
				e=input("please enter virtual grouph name: ")
				g=input("enter your paraition name (for example sdd2): ")
				l=int(input("enter how much size you want to reduce: "))
				os.system("lvreduce -r -L --size +{}G /dev/{}/{}".format(l,e,g))
				input("Press Enter to contineu")
				os.system("clear")
			elif lvmChoice == 4:
				y=input("Enter The partition name you want to increase: ")
				os.system("vgextend {} /dev/{}".format(e,y))
				input("Press Enter to contineu")
				os.system("clear")
			elif lvmChoice == 5:
				break
			else:
				print("Invalid Input Try Again")
	elif yourChoice == 5:
		while 5>4 :
			hadoopChoice = int(input("""What Do You Want in Hadoop
		1.Create Hadoop Master Name node
		2.Create Hadoop Slave Data node
		3.Create Hadoop Clinte Node.
		4.exit"""))
			if hadoopChoice == 1:
				dirName = input("enter directory name (for eg: name): ")
				check = sub.getstatusoutput("mkdir /{}".format(dirName))
				while check[0] != 0:
					print("this directory is exists")
					dirName = input("enter directory name again (for eg: name): ")
					check = sub.getstatusoutput("mkdir /{}".format(dirName))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.name.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(dirName))
				ip = (input("enter ip of your pc (for eg: 192.168.32.45): "))
				portNo = int(input("enter a port no (for eg: 9001): "))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip,portNo))
				os.system("hadoop namenode -format")
				sub.getoutput("hadoop-daemon.sh start namenode")
				print("your master name node is created successfully")
				input("Press Enter to contineu")
				os.system("clear")
			elif hadoopChoice == 2:
				dirName = input("enter directory name (for eg: name): ")
				check = sub.getstatusoutput("mkdir /{}".format(dirName))
				while check[0] != 0:
					print("this directory is exists")
					dirName = input("enter directory name again (for eg: name): ")
					check = sub.getstatusoutput("mkdir /{}".format(dirName))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.data.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(dirName))
				ip = (input("enter ip of your Master or Name Node pc (for eg: 192.168.32.45): "))
				portNo = int(input("enter port no (for eg: 9001): "))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip,portNo))
				sub.getoutput("hadoop-daemon.sh start datanode")
				print("your slave or data node is created successfully")
				input("Press Enter to contineu")
				os.system("clear")
			elif hadoopChoice == 3:
				ip = (input("enter ip of your Master or Name Node pc (for eg: 192.168.32.45): "))
				portNo = int(input("enter port no (for eg: 9001): "))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip,portNo))
				print("your clint is created successfully")
				input("Press Enter to contineu")
				os.system("clear")
			elif hadoopChoice == 4:
				break
			else:
				print("Invalid Input Try Again")
	elif yourChoice == 6:
		while 5>4:
			httpdChoice = int(input("""What Do You Want In HTTPD(Apache server):
		1.Install HTTPD(Apache) Server.
		2.Start Httpd Server.
		3.Status of Httpd Server.
		4.Stop Httpd Server.
		5.Unstall Httpd Server.
		6.Exit."""))
			if httpdChoice == 1:
				os.system("yum install httpd")
				print("Httpd is installed")
				input("Press Enter to contineu")
				os.system("clear")
			elif httpdChoice == 2:
				sub.getstatusoutput("systemctl start httpd")
				print("Httpd server is start")
				input("Press Enter to contineu")
				os.system("clear")
			elif httpdChoice ==3:
				os.system("systemctl status httpd")
				input("Press Enter to contineu")
				os.system("clear")
			elif httpdChoice == 4:
				sub.getstatusoutput("systemctl stop httpd")
				print("Httpd server is stoped")
				input("Press Enter to contineu")
				os.system("clear")
			elif httpdChoice == 5:
				os.system("yum remove httpd")
				print("Httpd is unstalled")
				input("Press Enter to contineu")
				os.system("clear")
			elif httpdChoice ==6:
				break
			else :
				print("Invalid Input Try Again")
	elif yourChoice == 7:
		exit()
	else:
		print("Invalid Input try again")

