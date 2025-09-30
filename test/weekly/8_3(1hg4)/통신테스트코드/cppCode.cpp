#include <iostream>
#include <string>
#include <stdexcept>
#include <winsock2.h>
#include <windows.h>
#define _USE_MATH_DEFINES
#define _WINSOCK_DEPRECATED_NO_WARNINGS

#pragma comment(lib, "ws2_32.lib")

// 닉네임을 사용자에 맞게 변경해 주세요.
#define NICKNAME "C++플레이어"

// 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
#define HOST "127.0.0.1"
#define PORT 1447

// 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
#define CODE_SEND 9901

void ErrorHandling(const std::string& message);
std::string ConvertToUTF8(const std::wstring& wstr);

int main()
{
	WSADATA wsaData;
	SOCKET hSocket;
	SOCKADDR_IN sockAddr;

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup failure.");

	hSocket = socket(PF_INET, SOCK_STREAM, 0);
	if (hSocket == INVALID_SOCKET)
		ErrorHandling("Socket Creating Failure.");

	memset(&sockAddr, 0, sizeof(sockAddr));
	sockAddr.sin_family = AF_INET;
	sockAddr.sin_addr.s_addr = inet_addr(HOST);
	sockAddr.sin_port = htons(PORT);

	std::cout << "Trying Connect: " << HOST << ":" << PORT << std::endl;
	if (connect(hSocket, (SOCKADDR*)&sockAddr, sizeof(sockAddr)) == SOCKET_ERROR)
		ErrorHandling("Connection Failure.");
	else
		std::cout << "Connected: " << HOST << ":" << PORT << std::endl;

	std::wstring wnickname = L"" NICKNAME "";
	std::string utf8Nickname = ConvertToUTF8(wnickname);
	std::string sendData = std::to_string(CODE_SEND) + "/" + utf8Nickname + "/";
	send(hSocket, sendData.c_str(), sendData.size(), 0);
	std::cout << "Ready to play!\n--------------------\n";

	closesocket(hSocket);
	WSACleanup();
	std::cout << "Connection Closed.\n--------------------\n";

	return 0;
}

void ErrorHandling(const std::string& message)
{
	std::cerr << message << std::endl;
	exit(1);
}

std::string ConvertToUTF8(const std::wstring& wstr)
{
	int size_needed = WideCharToMultiByte(CP_UTF8, 0, wstr.c_str(), -1, NULL, 0, NULL, NULL);
	std::string utf8Str(size_needed, 0);
	WideCharToMultiByte(CP_UTF8, 0, wstr.c_str(), -1, &utf8Str[0], size_needed, NULL, NULL);
	return utf8Str;
}
