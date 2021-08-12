import env from '~/libs/environment'

export default ({ app }, inject) => {
  inject('env', env)
}
