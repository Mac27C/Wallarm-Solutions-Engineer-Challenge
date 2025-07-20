
This project sets up a Wallarm Filtering Node in front of a FastAPI demo which is then used for integration to GoTestWAF to simulate attack traffic and test if the WAF worked.
First thing is creating the wallarm filtering node- wallarm svsDocker image: `wallarm/node:6.3.0`
Listens on port `8080`
Forwards requests to the backend service at `http://api-svc:8000`
Connected to Wallarm Cloud using your API token(that I created on the wallarm cloud platform)
Configured for the US API endpoint (`us1.api.wallarm.com`)

Second step run the API- I Built the FastAPI from local folder: `./src`
- Exposes port `8000`
- Receives traffic via the Wallarm WAF.

Third step is test the atttack and produce the report in the reports folder. `gotestwaf-svc` – Attack Traffic Generator
- Sends simulated malicious requests to test the WAF
- Outputs test reports to a mounted `./reports` folder.

For Testing I ran- docker run --rm -v ./reports:/app/reports --network wallarm-demo_wallarm-net -it wallarm/gotestwaf --url=http://wallarm-svc:80/demo --blockStatusCodes 200

Overall steps are FASTAPI built in docker('api-svc') then Wallarm WAF(' wallarm-svc') which proxies the traffic to the backend then finally have the GoTestWaf to simulate the attacks.

Issues I ran into was setting the coorect ports for the docker from(8080 to 8000 when you are trying to reach the FASTAPI). Another isssue was the WAF not forwarding and this fix was setting the NGINX_Backend-http://api-svc:8000





|      GoTestWAF           |
|   (simulated attacks)    |

            |

|    Wallarm WAF (8080)    |
|                          |
|  Filters malicious traffic|
            |
            v

|     FastAPI App (8000)   |
|       Returns Report    |

