 从yml启动pod

```
kubectl apply -f ***.yml
```

删除ConfigMap、pod

```
kubectl delete ConfigMap ***
kubectl delete pod ***
```



***映射端口号

Pod本身运行在K8s的内部私有网段，外界是无法直接访问的，想要对外暴露服务，需要用到一个专门的命令kubectl port-forward，它专门负责把本机的端口映射到目标对象的端口号，类似于Docker中的-p。

示例：

```
kubectl port-forward wp-pod 8080:80 &
```



创建反向代理的Nginx，让服务能够对访问。

```
docker run -d --rm \ --net=host \ -v /tmp/proxy.conf:/etc/nginx/conf.d/default.conf \ nginx:alpine

```



