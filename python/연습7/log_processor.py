import logging

log_filename = 'app.log'

# logging.basicConfig(
#     filename = log_filename,
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S"
# )

# logging.info("서버가 시작되었습니다.")
# logging.warning("메모리 사용량이 높습니다.")
# logging.error("데이터베이스 연결 실패")
# logging.error("파일을 찾을 수 없음")
# logging.warning("디스크 공간 부족")


# print("로그 파일이 생성 되었습니다.\n")

def print_log_by_level(filename, level):
    with open(filename, 'r') as f:
        lines = f.readlines()
        filtered = [line.strip() for line in lines if f" - {level} - " in line]
        if filtered:
            print(f"{level} 레벨 로그들 : ")
            for line in filtered:
                print(line)
            print()


print_log_by_level(log_filename, 'ERROR')
print_log_by_level(log_filename, 'WARNING')
