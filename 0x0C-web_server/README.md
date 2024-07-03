#  0x0C. Web server

##  Tasks
    -  Write a Bash script that transfers a file from our client to a server:
    Requirements:
      -  Accepts 4 parameters
        1.  The path to the file to be transferred
        2.  The IP of the server we want to transfer the file to
        3.  The username scp connects with
        4.  The path to the SSH private key that scp uses
      -  Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KE         if less than 3 parameters passed      
      -  scp must transfer the file to the user home directory ~/
      -  Strict host key checking must be disabled when using scp


     -  Readme:
        -  y on apt-get command
     Web servers are the piece of software generating and serving HTML pages, let’s install one!
     Requirements:
       - Install nginx on your web-01
       - server
       - Nginx should be listening on port 80
       - When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
       - As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
       - You can’t use systemctl for restarting nginx


   -  Readme:
     -  Replace a line with multiple lines with sed
     Configure your Nginx server so that /redirect_me is redirecting to another page.
     Requirements:
     -  The redirection must be a “301 Moved Permanently”
     -  You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
     -  Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task


  -  Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.
  Requirements:
  -  Nginx should be listening on port 80
  -  When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
-  The redirection must be a “301 Moved Permanently”
-  Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
