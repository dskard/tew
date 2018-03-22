import collections
import pexpect.replwrap
import pytest

pytestmark = [
               pytest.mark.dockercontainer,
             ]

# setup the output object with named attributes
BashOutput = collections.namedtuple(
                'BashOutput',
                ['stdout','stderr','returncode'])


class TestDockerContainer(object):

    def setup_method(self, method):

        # setup a shell to run commands in.
        self.shell = pexpect.replwrap.bash()


    def teardown_method(self, method):

        # clean up
        self.shell = None


    def run(self,cmd):

        separator = "this is the separator"

        # command string template to help store
        # stdout, stderr, returncode
        exec_cmd = """result=$(
    {{ stdout=$({cmd}) ; returncode=$?; }} 2>&1
    printf "{separator}"
    printf "%s\\n" "$stdout"
    exit "$returncode"
)
returncode=$?
var_out=${{result#*{separator}}}
var_err=${{result%{separator}*}}
""".format(cmd=cmd, separator=separator)

        # run the command
        # full output is stored in a variable named "result"
        self.shell.run_command(exec_cmd).strip()

        # capture returncode
        returncode = int(self.shell.run_command('echo ${returncode}',3).strip())

        # capture stdout
        stdout = self.shell.run_command('echo ${var_out}',3).strip()

        # capture stderr
        stderr = self.shell.run_command('echo ${var_err}',3).strip()

        return BashOutput(stdout,stderr,returncode)


    def test_pytest_exists_in_path(self):
        """make sure pytest is installed and in PATH."""

        command = "which pytest"

        # expected output from command
        expected = BashOutput(
                    stdout = "/usr/bin/pytest",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "cannot find pytest"


    def test_bats_exists_in_path(self):
        """make sure bats is installed and in PATH."""

        command = "which bats"

        # expected output from command
        expected = BashOutput(
                    stdout = "/usr/local/bin/bats",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "cannot find bats"


    def test_env_var_PYTHONDONTWRITEBYTECODE(self):
        """make sure PYTHONDONTWRITEBYTECODE environment variable is set."""

        command = "echo ${PYTHONDONTWRITEBYTECODE}"

        # expected output from command
        expected = BashOutput(
                    stdout = "1",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "PYTHONDONTWRITEBYTECODE not set"


    def test_env_var_PYTHONSTARTUP(self):
        """make sure PYTHONSTARTUP environment variable is set."""

        command = "[ `echo ${PYTHONSTARTUP} | wc -c` -gt 0 ] && echo 1 || echo 0"

        # expected output from command
        expected = BashOutput(
                    stdout = "1",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "PYTHONSTARTUP not set"


    def test_pystartup_file_exists(self):
        """make sure pystartup file exists."""

        command = "[ -r ${PYTHONSTARTUP} ] && echo 1 || echo 0"

        # expected output from command
        expected = BashOutput(
                    stdout = "1",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "cannot find ${PYTHONSTARTUP} file"


    def test_env_var_PYTHONUNBUFFERED(self):
        """make sure PYTHONUNBUFFERED environment variable is set."""

        command = "[ `echo ${PYTHONUNBUFFERED} | wc -c` -gt 0 ] && echo 1 || echo 0"

        # expected output from command
        expected = BashOutput(
                    stdout = "1",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "PYTHONUNBUFFERED not set"


    def test_python3_modules_pexpect(self):
        """python3 module pexpect is installed"""

        command = 'python3 -c "import pexpect"'

        # expected output from command
        expected = BashOutput(
                    stdout = "",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "Python 3 module 'pexpect' not installed"


    def test_python3_modules_pytest(self):
        """python3 module pytest is installed"""

        command = 'python3 -c "import pytest"'

        # expected output from command
        expected = BashOutput(
                    stdout = "",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "Python 3 module 'pytest' not installed"


    def test_python3_modules_selenium(self):
        """python3 module selenium is installed"""

        command = 'python3 -c "import selenium"'

        # expected output from command
        expected = BashOutput(
                    stdout = "",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "Python 3 module 'selenium' not installed"


    def test_python3_modules_selene(self):
        """python3 module selene is installed"""

        command = 'python3 -c "import selene"'

        # expected output from command
        expected = BashOutput(
                    stdout = "",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "Python 3 module 'selene' not installed"


    def test_python3_modules_zmq(self):
        """python3 module zmq is installed"""

        command = 'python3 -c "import zmq"'

        # expected output from command
        expected = BashOutput(
                    stdout = "",
                    stderr = "",
                    returncode = 0)

        # actual output from command
        actual = self.run(command)

        # compare actual with resulted
        assert expected == actual, "Python 3 module 'zmq' not installed"


