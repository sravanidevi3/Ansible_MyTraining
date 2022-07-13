- hosts: linux
  become_user: root
  become: true
  tasks:

  roles:
    - python_play
