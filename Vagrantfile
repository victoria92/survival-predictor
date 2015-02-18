# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

INSTALL_SCRIPT = "vagrant_data/install.sh"

Vagrant.require_version ">= 1.6.3"


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.ssh.forward_agent = true

  config.vm.synced_folder ".", "/home/vagrant/survival-predictor"
  config.vm.provision :shell, path: INSTALL_SCRIPT

  config.vm.network :private_network, ip: "192.168.13.13"
  config.vm.network "forwarded_port", guest: 1311, host: 1311

  config.vm.provider :virtualbox do |virtualbox|
    virtualbox.customize [
      'modifyvm', :id,
      '--memory', 512,
      '--cpus', 1
    ]
  end

end
