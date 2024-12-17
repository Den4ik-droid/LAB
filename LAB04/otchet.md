1. echo "den4ik-droid" 
2. pwd > ~/otchet/files/2.txt    
whoami >> ~/otchet/files/2.txt
3. ls -lai ~ > ~/otchet/files/3.txt 
4. echo "hedtrhyedt6y5ju" > ~/4.txt  
cat ~/4.txt > ~/4.md 
5. chmod go-r ~/4.txt  
6. chmod 755 ~/4.md
7. mv ~/4.txt ~/4.md ~/otchet/files
8. sudo chown root ~/otchet/files/4.md
9. sudo useradd -m -d /home/test_user -s /bin/zsh test_user
10. sudo passwd test_user
11. 
12. cat /etc/passwd > ~/otchet/files/12.txt   
13. chmod 666 ~/otchet/files/12.txt
14. su -P test_user
15. echo "test_user: $(whoami)" >> /home/den4ik-droid/otchet/files/12.txt 
echo "/home/test_user: $(pwd)" >> /home/den4ik-droid/otchet/files/12.txt
15. exit
17. sudo su 
18. cd /home/test_user
echo "test_user: $(whoami)" >> /home/den4ik-droid/otchet/files/12.txt 
echo "/home/test_user: $(pwd)" >> /home/den4ik-droid/otchet/files/12.txt
exit
19. tail -n 2 ~/otchet/files/12.txt
20. sudo userdel -r test_user 
21. find ~ -maxdepth 2 -type d -empty > ~/otchet/files/21.txt
22. sudo find / -maxdepth 3 -type f -name 'dev*' -user root > ~/otchet/files/22.txt 
23. mkdir -p ~/test_find/time ~/test_find/permissions
24. touch ~/test_find/time/one.txt
touch -a -d "2024-01-01 00:00:00" ~/test_find/time/one.txt
touch ~/test_find/time/two.txt
touch -m -d "2024-10-14 00:00:00" ~/test_find/time/two.txt
25. touch ~/test_find/permissions/cant_write.txt 
touch ~/test_find/permissions/cant_execute.txt
chmod a-w ~/test_find/permissions/cant_write.txt
chmod a+x ~/test_find/permissions/cant_execute.txt 
26. find ~/test_find -type f -empty -atime -180 -delete
27. find ~/test_find -type f -perm 755 -exec chmod a-x {} +
28. man ls > ~/otchet/files/man_ls.txt
29. grep -n "^$" ~/otchet/files/man_ls.txt
30. grep -E "[0-9]+" ~/otchet/files/man_ls.txt
31. grep -i 'author' ~/otchet/files/man_ls.txt > ~/otchet/files/31.txt
32. wc -l ~/otchet/files/man_ls.txt 
du -sh ~/otchet/files/man_ls.txt 
33. ps -u $USER > ~/otchet/files/33.txt 
34. nano
35. pgrep nano
36. pkill nano
37. htop
