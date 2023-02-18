from modules.password import TestGeneticPassword


if __name__ == '__main__':
    genes = 'abcdefghijklmnñopqrstuvwxyzAVCDEFGHIJKLMNÑOPWRSTUVWXYZ0123456789-, '
    password = "This is a very large Password, with number as 1,2,3"
    TestGeneticPassword(password, genes).getBest()
