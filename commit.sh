# CTFd
rm -rf data/ctfd/CTFd/uploads/
cp -R -i tmp-data/ctfd/CTFd/uploads/ data/ctfd/CTFd/uploads/
cp -i tmp-data/ctfd/CTFd/ctfd.db data/ctfd/CTFd/ctfd.db
# Gitea
rm -rf data/gitea/git
cp -R -i tmp-data/gitea/git data/gitea/git
rm -rf data/gitea/gitea/conf
cp -R -i tmp-data/gitea/gitea/conf data/gitea/gitea/conf
cp -i tmp-data/gitea/gitea/gitea.db data/gitea/gitea/gitea.db