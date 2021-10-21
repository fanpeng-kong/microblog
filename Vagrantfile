Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
<<<<<<< HEAD
=======
  if Vagrant.has_plugin?("vagrant-vbguest") then
    config.vbguest.auto_update = false
  end
>>>>>>> 6b2ce75 (Chapter 18: Deployment on Heroku)
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
end
