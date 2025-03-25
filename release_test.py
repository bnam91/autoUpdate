import os
from release_updater import ReleaseUpdater

# 환경 변수나 설정 파일에서 값 읽기
owner = os.environ.get("GITHUB_OWNER", "bnam91")
repo = os.environ.get("GITHUB_REPO", "autoUpdate")

def main():
    try:
        updater = ReleaseUpdater(owner=owner, repo=repo)
        update_success = updater.update_to_latest()
        
        if update_success:
            print("프로그램을 실행합니다...")
        else:
            print("업데이트 실패, 이전 버전으로 계속 진행합니다...")
        
        # 업데이트 결과와 상관없이 실행되는 코드
        run_program()
        
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}")
        # 중요한 예외는 로깅하거나 오류 보고 시스템에 전송할 수 있음

def run_program():
    # 실제 프로그램 코드를 별도 함수로 분리
    print("Hello, GitHub!")

if __name__ == "__main__":
    main() 