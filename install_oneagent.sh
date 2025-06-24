# This should be run preferably inside a container, unless one really wants to add the Linux machine to the Dynatrace ecosystem

wget -O Dynatrace-OneAgent-Linux-x86-1.303.50.20241118-133432.sh "https://${DYNATRACE_ENVIRONMENT_ID}.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86" --header="Authorization: Api-Token ${DYNATRACE_API_TOKEN}"

/bin/sh Dynatrace-OneAgent-Linux-x86-1.303.50.20241118-133432.sh --set-monitoring-mode=fullstack --set-app-log-content-access=true
