import subprocess as sub
import os
os.system("tput setaf 6")
print("------------------------------------------------------------------------------------------------------------------- \n")
print("\t \t Welcome, This is a Menu Program. It will reduce your Work & Time.")
print(" \n -------------------------------------------------------------------------------------------------------------------")
os.system("tput setaf 7")
while 5>4 :
	yourChoice = int(input("""Select the Technology you want Install in your PC :
	1.Configure YUM.
	2.Docker.
	3.Create Partition.
	4.LVM.
	5.Hadoop.
	6.HTTPd.
	7.Exit. """))
	
	if yourChoice == 1:
		print("Please wait a second....!!!!")
		a = sub.getstatusoutput("yum install firefox")
		if a[0] == 0:
			print("Yum is already configured in this system.")
			input("Press Enter to continue")
			os.system("clear")
		else:
			sub.getstatusoutput("echo '[dvd1] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream \ngpgcheck=0 \n\n[dvd2] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS \ngpgcheck=0' > yumconfi.repo | mv yumconfi.repo /etc/yum.repos.d/")
			print("Yum is configured in yumcondi.repo file")
			input("Press Enter to Continue")
			os.system("clear")
	
	elif yourChoice == 2:
		while 5>4 :
			dockerInput=int(input("""Which operations you want to perform in Docker ? :
			1.Install Docker.
			2.Start Docker service.
			3.Status of Docker.
			4.Download Docker Image in your OS.
			5.See the list of Docker Images installed in your OS.
			6.Install Docker Image in your PC.
			7.Boot any os which is previously installed.
			8.Terminate Docker Image.
			9.Exit. """))
		
			if dockerInput == 1:
				os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")		
				os.system("dnf install docker-ce --nobest")
				input("Press Enter to Continue")
				os.system("clear")
			elif dockerInput == 2:
				os.system("systemctl start docker")
				input("Press Enter to Continue")
				os.system("clear")
			elif dockerInput == 3:
				os.system("systemctl status docker")
				input("Press Enter to Continue")
				os.system("clear")
			elif dockerInput == 4:
				sub.getoutput("systemctl start docker")
				imgName = input("Enter full name of image which you want to download (for eg: centos:7): ")
				os.system("docker pull {}".format(imgName))
				os.system("docker images")
				input("Press Enter to Continue")
				os.system("clear")
			elif dockerInput == 5:
				os.system("docker images")
				input("Press Enter to Continue")
				os.system("clear")
			elif dockerInput == 6:
				os.system("docker image")
				imgName = input("Enter full name of Docker Image(For eg: centos:7): ")	
				osName = input("Enter Your Image Name(for eg:CentOSv7): ")
				os.system("docker run -it -name {} {}".format(osName,imgName))
				input("Press Enter to Continue")
				os.system("clear")
			elif dockerInput == 7:
				os.system("docker ps")
				sub.getoutput("systemctl start docker")
				dockerId = input("Enter any OS Name or OS ID to start the Docker Service: ")
				so.system("docker start {}".format(dockerId))
				os.system("docker attach {}".format(dockerId))
				input("Press Enter to Continue")
				os.system("clear")
			elif dockerInput == 8:
				os.system("docker ps")
				sub.getoutput("systemctl start docker")
				dockerId = input("Enter any OS Name or OS ID to Remove Docker Image: ")
				so.system("docker rm {}".format(dockerId))
				input("Press Enter to Continue")
				os.system("clear")
			elif dockerInput == 9:
				break
	elif yourChoice == 3:
		while 5>4 :
			partitionChoice = int(input("""Which Partition Concept you want to perform ?:
			1.Create the Partition.
			2.See all the Disk present in your PC.
			3.See all Mounted Disks present in your PC.
			4.Exit. """))
		
			if partitionChoice == 1:
				os.system("fdisk -l")
				diskName = input("Enter Disk Name which is used for creating disk partition (like sda,sdc,sdb etc) :")
				print(""" ----- FOR HELP -----
				p. To see the details of your disk.
				n. To create new partition.
				d. To delete partition.
				w. To save changes. """)
				
				os.system("fdisk /dev/{}".format(diskName))
				os.system("udevadm settle")
				os.system("lsblk")
				diskNumber = int(input("How many partition you want to create ?: "))
				if diskNumber == 0:
					break
				else :
					for i in range(diskNumber-1):
						name = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth']
						partLoca = input("Enter your {} partition name which you created (like sdc1): ".format(name[i]))
						partName = input("In which directory you want to mount your partition: ")
						confirm = sub.getstatusoutput("mkdir {}".format(partName))
						while confirm[0] != 0:
							partName = input("This directory {} exists. Please re-type the directory name: ".format(partName))
							confirm = sub.getstatusoutput("mkdir {}".format(partName))
						os.system("mkfs.ext4 /dev/{}".format(partLoca))
						os.system("mount /dev/{} {}".format(partLoca,partName))	
						input("Press Enter to Continue")
						os.system("clear")
			elif partitionChoice ==2:
				os.system("fdisk -l")
				input("Press Enter to Continue")
				os.system("clear")
			elif partitionChoice ==3:
				os.system("df -h")
				input("Press Enter to Continue")
				os.system("clear")
			elif partitionChoice ==4:
				break
			else:
				print("Invalid input, please try again....!!!!")
	elif yourChoice == 4:
		while 5>4 :
			lvmChoice = int(input("""Which operations you want to perform in LVM ?
			1.Create or Delete Logical Partition.
			2.Extend Partition Size.
			3.Reduce Partition Size.
			4.Extend Virtual Group Size.
			5.Exit."""))
			
			if lvmChoice == 1:
				os.system("fdisk -l")
				b=int(input("Enter how much storage partition you want to create:"))
				c=[]
				for i in range(b):
					d=input("Enter the name of storage {}".format(i+1))
					c.append(d)
					os.system("pvcreate /dev/{}".format(d))
				e=input("Please enter the Virtual Group name: ")
				os.system("vgcreate {} /dev/{}".format(e,c[0]))
				x = range(b)
				x.pop(0)
				for p in x:
					os.system("vgextend {} /dev/{}".format(e,c[p]))
				f=int(input("Enter the Partition Size: "))
				g=input("Enter your Paraition Name: ")
				os.system("lvcreate --size {}G --name {} {}".format(f,g,e))
				os.system("mkfs.ext4 /dev/{}/{}".format(e,g))
				h=input("Enter the Directory Name where you want to mount recently created partition: ")
				os.system("mkdir {}".format(h))
				os.system("mount /dev/{}/{} {}".format(e,g,h))
				print("Your Partition is Created Successfully")
				a=input("Do you want to see details of your storage? (y/n): ")
				if a in 'y':
					os.system("lvdisplay {}/{}".format(e,g))
				input("Press Enter to Continue")
				os.system("clear")
			elif lvmChoice == 2:
				e=input("Please enter the Virtual Group Name: ")
				g=input("Please enter your Paraition Name (for example sdd2): ")
				l=int(input("Enter how much size you want to increase: "))
				os.system("lvextend --size +{}G /dev/{}/{}".format(l,e,g))
				os.system("resize2fs /dev/{}/{}".format(e,g))
				input("Press Enter to Continue")
				os.system("clear")
			elif lvmChoice == 3:
				e=input("Please enter the Virtual Group Name: ")
				g=input("Please enter your Paraition Name(for example sdd2): ")
				l=int(input("Enter how much size you want to reduce: "))
				os.system("lvreduce -r -L --size +{}G /dev/{}/{}".format(l,e,g))
				input("Press Enter to Continue")
				os.system("clear")
			elif lvmChoice == 4:
				y=input("Enter the Partition Name you want to increase: ")
				os.system("vgextend {} /dev/{}".format(e,y))
				input("Press Enter to Continue")
				os.system("clear")
			elif lvmChoice == 5:
				break
			else:
				print("Invalid input, please try again....!!!!")
	elif yourChoice == 5:
		while 5>4 :
			hadoopChoice = int(input("""Which operations you want to perform in Hadoop ?
			1.Create Hadoop Master Name node.
			2.Create Hadoop Slave Data node.
			3.Create Hadoop Client Node.
			4.Exit. """))
			
			if hadoopChoice == 1:
				dirName = input("Enter Directory Name (for eg: name): ")
				check = sub.getstatusoutput("mkdir /{}".format(dirName))
				while check[0] != 0:
					print("This directory name already exists. Please enter another name...")
					dirName = input("Enter the Directory name again (for eg: name): ")
					check = sub.getstatusoutput("mkdir /{}".format(dirName))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.name.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(dirName))
				ip = (input("Enter IP address of your PC (for eg: 192.168.32.45): "))
				portNo = int(input("Enter the Port no. (for eg: 9001): "))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip,portNo))
				os.system("hadoop namenode -format")
				sub.getoutput("hadoop-daemon.sh start namenode")
				print("Your Master i.e, Name node is created successfully.")
				input("Press Enter to Continue")
				os.system("clear")
			elif hadoopChoice == 2:
				dirName = input("Enter Directory name (for eg: name): ")
				check = sub.getstatusoutput("mkdir /{}".format(dirName))
				while check[0] != 0:
					print("This directory name already exists. Please enter another name...")
					dirName = input("Enter Directory name again (for eg: name): ")
					check = sub.getstatusoutput("mkdir /{}".format(dirName))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.data.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(dirName))
				ip = (input("Enter IP of your Master or Name Node PC (for eg: 192.168.32.45): "))
				portNo = int(input("Enter the Port no. (for eg: 9001): "))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip,portNo))
				sub.getoutput("hadoop-daemon.sh start datanode")
				print("Your Slave or Data node is created successfully.")
				input("Press Enter to Continue")
				os.system("clear")
			elif hadoopChoice == 3:
				ip = (input("Enter IP of your Master or Name Node PC (for eg: 192.168.32.45): "))
				portNo = int(input("Enter the Port no. (for eg: 9001): "))
				sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip,portNo))
				print("Your Client is created successfully.")
				input("Press Enter to Continue")
				os.system("clear")
			elif hadoopChoice == 4:
				break
			else:
				print("Invalid input, please try again....!!!!")
	elif yourChoice == 6:
		while 5>4:
			httpdChoice = int(input("""Which operation you want to perform in HTTPd(Apache server):
			1.Install HTTPd(Apache) Server.
			2.Start HTTPd Server.
			3.Status of HTTPd Server.
			4.Stop HTTPd Server.
			5.Uninstall HTTPd Server.
			6.Exit."""))
			
			if httpdChoice == 1:
				os.system("yum install httpd")
				print("HTTPd is installed successfully.")
				input("Press Enter to Continue")
				os.system("clear")
			elif httpdChoice == 2:
				sub.getstatusoutput("systemctl start httpd")
				print("HTTPd server is started successfully.")
				input("Press Enter to Continue")
				os.system("clear")
			elif httpdChoice ==3:
				os.system("systemctl status httpd")
				input("Press Enter to Continue")
				os.system("clear")
			elif httpdChoice == 4:
				sub.getstatusoutput("systemctl stop httpd")
				print("HTTPd server is stopped successfully.")
				input("Press Enter to Continue")
				os.system("clear")
			elif httpdChoice == 5:
				os.system("yum remove httpd")
				print("HTTPd is Uninstalled successfully.")
				input("Press Enter to Continue")
				os.system("clear")
			elif httpdChoice ==6:
				break
			else :
				print("Invalid input, please try again....!!!!")
	elif yourChoice == 7:
		exit()
	else:
		print("Invalid input, please try again....!!!!")

