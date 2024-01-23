*** Settings ***
Library     RPA.FileSystem
Library     RPA.HTTP
Library     RPA.Robocorp.Vault

*** Variables ***
${AUDIO_FILE}    output.wav
${TEXT_FILE}     output.txt
*** Keywords ***
Capture Audio
    [Documentation]    Capture audio from the microphone
    ${audio_file} =    Record Audio    5s
    [Return]    ${audio_file}

Convert Speech to Text
    [Arguments]    ${audio_file}
    [Documentation]    Use Google Speech Recognition to convert audio to text
    ${text} =    Recognize Speech    ${audio_file}
    [Return]    ${text}

Write Text to File
    [Arguments]    ${text}
    [Documentation]    Write the recognized text to a file
    Write Text File    ${TEXT_FILE}    ${text}

*** Tasks ***
Interpret Human Voice and Write to File
    ${audio_file} =    Capture Audio
    ${text} =    Convert Speech to Text    ${audio_file}
    Write Text to File    ${text}
    Log    Text written to ${TEXT_FILE}
