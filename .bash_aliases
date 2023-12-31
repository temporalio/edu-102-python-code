alias workspace="cd ${GITPOD_REPO_ROOT}"
alias webui="gp preview $(gp url 8080)"
alias ex1="cd ${GITPOD_REPO_ROOT}/exercises/durable-execution/practice"
alias ex2="cd ${GITPOD_REPO_ROOT}/exercises/testing-code/practice"
alias ex3="cd ${GITPOD_REPO_ROOT}/exercises/debug-activity/practice"
alias ex1s="cd ${GITPOD_REPO_ROOT}/exercises/durable-execution/solution"
alias ex2s="cd ${GITPOD_REPO_ROOT}/exercises/testing-code/solution"
alias ex3s="cd ${GITPOD_REPO_ROOT}/exercises/debug-activity/solution"
export PATH="$PATH:/home/gitpod/.temporalio/bin"
echo "temporal configured! try typing temporal -v"
echo "Your workspace is located at: ${GITPOD_REPO_ROOT}"
echo "Type the command     workspace      to return to the workspace directory at any time."