import speedtest
import argparse
import json
import datetime

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    results = {
        "server": st.best["sponsor"] + " (" + st.best["name"] + ", " + st.best["country"] + ")",
        "isp": st.results.client["isp"],
        "ping": f"{st.results.ping} ms",
        "download_speed": f"{st.download() / 1_000_000:.2f} Mbps",
        "upload_speed": f"{st.upload() / 1_000_000:.2f} Mbps",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return results

def save_log(results):
    with open("speed_test.log", "a") as log_file:
        log_file.write(json.dumps(results) + "\n")

def main():
    parser = argparse.ArgumentParser(description="Advanced Network Speed Test CLI Tool")
    parser.add_argument("--log", action="store_true", help="Save results to a log file")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()
    
    results = test_speed()
    
    if args.json:
        print(json.dumps(results, indent=4))
    else:
        print("\n".join([f"{key.replace('_', ' ').title()}: {value}" for key, value in results.items()]))

    if args.log:
        save_log(results)

if __name__ == "__main__":
    main()
