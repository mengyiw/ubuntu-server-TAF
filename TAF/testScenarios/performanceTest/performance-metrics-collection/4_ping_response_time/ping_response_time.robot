*** Settings ***
Documentation   Measure the ping response time
...             Measure the ping response time of ping API for each edgex service
...             Measure the ping execution time from creating event by device-virtual until export-distro send event to a MQTT broker
Library         TAF/testCaseModules/keywords/setup/edgex.py
Library         TAF/testCaseModules/keywords/performance-metrics-collection//PingResponse.py
Resource        TAF/testCaseModules/keywords/common/commonKeywords.robot
Suite Setup     Run keywords    Setup Suite
                ...             AND  Deploy EdgeX  PerformanceMetrics
                ...             AND  Run Keyword if  $SECURITY_SERVICE_NEEDED == 'true'  Get Token
Suite Teardown  Run Keywords  Run Keyword if  $SECURITY_SERVICE_NEEDED == 'true'  Remove Token
                ...      AND  Run Keyword And Ignore Error  Shutdown services

*** Variables ***
${SUITE}          Measure the ping response time
${LOG_FILE_PATH}  ${WORK_DIR}/TAF/testArtifacts/logs/performance-metric-collection-ping.log


*** Test Cases ***
Measure the ping response time
    ${DATA_RES_LIST}=  Ping API for service  core-data  ${CORE_DATA_PORT}
    Record response   edgex-core-data              ${DATA_RES_LIST}

    ${METADATA_RES_LIST}=  Ping API for service  core-metadata  ${CORE_METADATA_PORT}
    Record response   edgex-core-metadata          ${METADATA_RES_LIST}

    ${COMMAND_RES_LIST}=  Ping API for service  core-command  ${CORE_COMMAND_PORT}
    Record response   edgex-core-command           ${COMMAND_RES_LIST}

    ${SCHEDULER_RES_LIST}=  Ping API for service  support-scheduler  ${SUPPORT_SCHEDULER_PORT}
    Record response   edgex-support-scheduler      ${SCHEDULER_RES_LIST}

    ${NOTIFICATIONS_RES_LIST}=  Ping API for service  support-notifications  ${SUPPORT_NOTIFICATIONS_PORT}
    Record response   edgex-support-notifications  ${NOTIFICATIONS_RES_LIST}

    ${SYS_MGMT_RES_LIST}=  Ping API for service  sys-mgmt-agent  ${SYS_MGMT_AGENT_PORT}
    Record response   edgex-sys-mgmt-agent          ${SYS_MGMT_RES_LIST}

    ${DEVICE_REST_RES_LIST}=  Ping API for service  device-rest  ${DEVICE_REST_PORT}
    Record response   edgex-device-rest             ${DEVICE_REST_RES_LIST}

    ${APP_SERVICE_RES_LIST}=  Ping API for service  app-service  ${APP_SERVICE_RULES_PORT}
    Record response   edgex-app-rules-engine        ${APP_SERVICE_RES_LIST}

    ${DEVICE_VIRTUAL_RES_LIST}=  Ping API for service  device-virtual  ${DEVICE_VIRTUAL_PORT}
    Record response   edgex-device-virtual           ${DEVICE_VIRTUAL_RES_LIST}

Show all services response time
    show full response time report

Show aggregation report
    show the aggregation report

*** Keywords ***
Response time is less than threshold setting
    [Arguments]  ${service}  ${response}
    ${response_time}=    evaluate  ${response}[seconds] * 1000
    ${compare_result}  evaluate   ${response_time} < ${PING_RES_THRESHOLD}
     [Return]  ${compare_result}

Ping API for service
    [Arguments]  ${service_name}  ${service_port}
    @{RES_LIST}=  Create List
    ${failure_count}  set variable  0
    FOR  ${index}  IN RANGE  0  ${PING_RES_LOOP_TIMES}
        ${res}  Ping api request  ${service_port}  ${jwt_token}
        ${status}  ${value}  run keyword and ignore error  Response time is less than threshold setting  ${service_name}  ${res}
        APPEND TO LIST  ${RES_LIST}     ${res}
        ${failure_count}  Run Keyword If  ${value} == False  Evaluate  ${failure_count}+1
                          ...       ELSE  set variable  ${failure_count}
    END
    Run Keyword If  ${failure_count} > ${ALLOWABLE_OUTLIER}  Run Keyword And Continue On Failure
    ...             Fail  ${failure_count} times that response time is over than ${PING_RES_THRESHOLD}ms when ping ${service_name}
    [Return]  ${RES_LIST}
