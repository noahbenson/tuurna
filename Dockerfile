
FROM quay.io/jupyter/datascience-notebook:python-3.12

USER root

RUN apt-get update --yes \
 && apt-get dist-upgrade --yes \
 && apt-get install emacs-nox nodejs npm --yes

COPY ./ "/home/${NB_USER}/tuurna/"
RUN fix-permissions "/home/${NB_USER}/tuurna/"

USER ${NB_USER}

RUN ln -s "/home/${NB_USER}/tuurna/nb" "/home/${NB_USER}/nb"
RUN cd "/home/${NB_USER}/tuurna/" \
 && pip install -e . \
 && pip install 'jupyter-book<2' \
 && python -c 'import matplotlib, numpy, scipy, icepool, tuurna'
