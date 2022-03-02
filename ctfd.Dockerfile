FROM ctfd/ctfd:3.4.1
COPY --chown=ctfd:ctfd data/ctfd/CTFd/ctfd.db /opt/CTFd/CTFd/ctfd.db
COPY --chown=ctfd:ctfd data/ctfd/CTFd/uploads/ /opt/CTFd/CTFd/uploads/
LABEL version="${TAG}"