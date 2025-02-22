1. 关闭swap
2. 关闭SELinux
3. 关闭firewalld
4. Check required ports
For example:
nc 127.0.0.1 6443
https://v1-28.docs.kubernetes.io/docs/reference/networking/ports-and-protocols/
5. 
registry.k8s.io/kube-apiserver:v1.28.15
registry.k8s.io/kube-controller-manager:v1.28.15
registry.k8s.io/kube-scheduler:v1.28.15
registry.k8s.io/kube-proxy:v1.28.15
registry.k8s.io/pause:3.9
registry.k8s.io/etcd:3.5.15-0
registry.k8s.io/coredns/coredns:v1.10.1

6. install containerd
(1) install containerd
Download the containerd-<VERSION>-<OS>-<ARCH>.tar.gz archive from https://github.com/containerd/containerd/releases , verify its sha256sum, and extract it under /usr/local:
$ tar Cxzvf /usr/local containerd-1.6.2-linux-amd64.tar.gz
bin/
bin/containerd-shim-runc-v2
bin/containerd-shim
bin/ctr
bin/containerd-shim-runc-v1
bin/containerd
bin/containerd-stress
(2) install runc
Download the runc.<ARCH> binary from https://github.com/opencontainers/runc/releases , verify its sha256sum, and install it as /usr/local/sbin/runc.
$ install -m 755 runc.amd64 /usr/local/sbin/runc

(3) Installing CNI plugins
Download the cni-plugins-<OS>-<ARCH>-<VERSION>.tgz archive from https://github.com/containernetworking/plugins/releases , verify its sha256sum, and extract it under /opt/cni/bin:
$ mkdir -p /opt/cni/bin
$ tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.1.1.tgz
./
./macvlan
./static
./vlan
./portmap
./host-local
./vrf
./bridge
./tuning
./firewall
./host-device
./sbr
./loopback
./dhcp
./ptp
./ipvlan
./bandwidth

(4) install nerdctl
tar Cxzvvf /usr/local/bin nerdctl-2.0.3-linux-arm64.tar.gz
https://github.com/containerd/nerdctl/releases/tag/v2.0.3

7. 
Steps to Resolve
	1.	Remove Existing Manifests
Since the manifests already exist from a previous failed attempt, you can safely remove them:
rm -f /etc/kubernetes/manifests/kube-apiserver.yaml
rm -f /etc/kubernetes/manifests/kube-controller-manager.yaml
rm -f /etc/kubernetes/manifests/kube-scheduler.yaml
rm -f /etc/kubernetes/manifests/etcd.yaml