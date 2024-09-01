# 使用官方的Nginx镜像作为基础镜像
FROM nginx:alpine

# 将本地的nginx.conf文件复制到容器中
COPY nginx.conf /etc/nginx/nginx.conf

# 将应用文件复制到Nginx的默认静态文件目录
COPY app/ /usr/share/nginx/html/

# 暴露80端口
EXPOSE 80

# 启动Nginx
CMD ["nginx", "-g", "daemon off;"]