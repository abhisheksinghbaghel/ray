import argparse
from ray.job_submission import JobSubmissionClient

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Stop a Ray job.')
    parser.add_argument('job_id', type=str, help='The ID of the Ray job to stop.')
    parser.add_argument('--address', type=str, default='http://127.0.0.1:8265',
                        help='The address of the Ray cluster.')
    args = parser.parse_args()

    # Initialize the Ray JobSubmissionClient
    client = JobSubmissionClient(args.address)

    # Attempt to stop the specified job
    try:
        result = client.stop_job(args.job_id)
        if result:
            print(f"Job {args.job_id} has been successfully stopped.")
        else:
            print(f"Job {args.job_id} was not running.")
    except RuntimeError as e:
        print(f"Failed to stop job {args.job_id}: {e}")

if __name__ == "__main__":
    main()
